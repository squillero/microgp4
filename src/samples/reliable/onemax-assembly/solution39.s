    .file   "solution.c"
    .text
    .globl  _darwin
    .def    _darwin;        .scl    2;      .type   32;     .endef
_darwin:
LFB17:
    .cfi_startproc
    pushl   %ebp
    .cfi_def_cfa_offset 8
    .cfi_offset 5, -8
    movl    %esp, %ebp
    .cfi_def_cfa_register 5

    movl	$31045, %eax
    movl	$-20525, %ebx
    movl	$-249, %ecx
    movl	$-7019, %edx

    or %ecx, %ecx
    shl $217, %ecx
    or %ebx, %ecx
    shl $52, %eax
    and %ecx, %ecx
    or %edx, %ebx
    jo n15
    shl $21, %ecx
    jmp n18
    and %eax, %eax
    cmp %edx, %ecx
    jno n17
n15:
    shr $73, %edx
    add %ebx, %eax
n17:
    sub %ecx, %ecx
n18:
    jnc n23
    add %ebx, %edx
    and %ecx, %ecx
    add %ebx, %ecx
    shr $160, %ecx
n23:
    sub %eax, %eax
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
