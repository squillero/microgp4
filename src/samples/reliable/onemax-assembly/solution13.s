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

    movl	$22759, %eax
    movl	$-25676, %ebx
    movl	$-9823, %ecx
    movl	$22634, %edx

    jno n15
    shr $142, %ebx
    shl $13, %ecx
    add %ebx, %ecx
    jne n18
    shl $3, %ebx
    jnz n28
    shl $35, %ebx
    shr $46, %ebx
    shl $214, %edx
    and %ebx, %ecx
    shl $166, %eax
n15:
    ja n20
    sub %eax, %eax
    and %edx, %edx
n18:
    shl $226, %edx
    and %ebx, %eax
n20:
    shl $220, %eax
    jne n31
    or %ecx, %eax
    shr $202, %eax
    add %ebx, %ecx
    sub %ebx, %ecx
    jne n29
    shr $3, %edx
n28:
    shl $89, %ebx
n29:
    jnc n30
n30:
    jno n31
n31:
    movl	%eax, -4(%ebp)
    movl	-4(%ebp), %eax
    leave
    .cfi_restore 5
    .cfi_def_cfa 4, 4
    ret
    .cfi_endproc
LFE17:
   .ident  "GCC: (MinGW.org GCC-8.2.0-5) 8.2.0"
