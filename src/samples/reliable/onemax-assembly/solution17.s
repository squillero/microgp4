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

    movl	$29256, %eax
    movl	$26902, %ebx
    movl	$-18217, %ecx
    movl	$20755, %edx

    jo n26
    add %edx, %eax
    or %ecx, %ebx
    jnc n12
    and %ebx, %eax
    shl $50, %ecx
    shr $70, %eax
    and %edx, %ebx
    cmp %edx, %edx
n12:
    xor %eax, %eax
    add %ecx, %ebx
    shr $216, %eax
    shl $121, %ecx
    add %eax, %ebx
    jnc n38
    jmp n33
    shr $56, %edx
    jmp n38
    add %ebx, %ebx
    jne n36
    shr $180, %ebx
    xor %edx, %ebx
    cmp %eax, %ecx
n26:
    shr $10, %edx
    jo n28
n28:
    shl $191, %ecx
    shr $182, %eax
    jc n34
    cmp %eax, %ecx
    jnz n33
n33:
    jc n38
n34:
    and %ebx, %edx
    cmp %edx, %ebx
n36:
    shr $32, %edx
    ja n38
n38:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
